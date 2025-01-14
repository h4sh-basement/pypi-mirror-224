from polly.auth import Polly
from polly.errors import (
    InvalidParameterException,
    error_handler,
    InvalidPathException,
    AccessDeniedError,
)
from polly import helpers
from polly import constants as const
import logging
import pandas as pd
import json
import os
from polly.help import example
from polly.tracking import Track


class Workspaces:
    """
    This class contains functions to interact with workspaces on Polly. Users can create a workspace, fetch list\
 of workspaces, upload data to workspace and download data from workspace. To get started, users need to \
initialize a object that can use all function and methods of Workspaces class.
    Args:
        token (str): Authentication token from polly
    Usage:
        from polly.workspaces import Workspaces

        workspaces = Workspaces(token)
    """

    example = classmethod(example)

    def __init__(self, token=None, env="", default_env="polly") -> None:
        # check if COMPUTE_ENV_VARIABLE present or not
        # if COMPUTE_ENV_VARIABLE, give priority
        env = helpers.get_platform_value_from_env(
            const.COMPUTE_ENV_VARIABLE, default_env, env
        )
        self.session = Polly.get_session(token, env=env)
        self.base_url = f"https://v2.api.{self.session.env}.elucidata.io"
        self.resource_url = f"{self.base_url}/workspaces"
        if self.session.env == "polly":
            self.env_string = "prod"
        elif self.session.env == "testpolly":
            self.env_string = "test"
        else:
            self.env_string = "devenv"

    @Track.track_decorator
    def create_workspace(self, name: str, description=None):
        """
        This function create workspace on Polly.
        Returns a Dictionary object like this
                        {
                        'id': 9999,
                        'name': 'rrrrr',
                        'active': True,
                        'description': 'for docu',
                        'created_time': '2022-03-16 11:08:47.127260',
                        'last_modified': '2022-03-16 11:08:47.127260',
                        'creator': 1127,
                        'project_property': {
                            'type': 'workspaces',
                            'labels': ''
                        },
                        'organisation': 1
                        }
        Args:
              name (str): name of the workspace
              description (str, optional): general information about workspace


        """
        url = self.resource_url
        payload = {
            "data": {
                "type": "workspaces",
                "attributes": {
                    "name": name,
                    "description": description,
                    "project_property": {"type": "workspaces", "labels": ""},
                },
            }
        }
        response = self.session.post(url, data=json.dumps(payload))
        error_handler(response)
        attributes = response.json()["data"]["attributes"]
        logging.basicConfig(level=logging.INFO)
        logging.info("Workspace Created !")
        return attributes

    @Track.track_decorator
    def fetch_my_workspaces(self):
        """
        This function fetch workspaces from Polly.
        Args:
              None
        Returns:
              A table with workspace specific attributes
        """
        all_details = self._fetch_workspaces_iteratively()
        pd.set_option("display.max_columns", 20)
        dataframe = pd.DataFrame.from_dict(
            pd.json_normalize(all_details), orient="columns"
        )
        dataframe.rename(
            columns={"id": "Workspace_id", "name": "Workspace_name"}, inplace=True
        )
        df = dataframe.sort_values(by="last_modified", ascending=False)
        df = df.reset_index()
        df.drop("index", axis=1, inplace=True)
        return df

    def _fetch_workspaces_iteratively(self):
        """
        Fetch all workspaces iteratively by making api calls until links is None.
        """
        url = self.resource_url
        all_details = []
        while True:
            response = self.session.get(url)
            error_handler(response)
            data = response.json()["data"]
            for workspace_details in data:
                self._modify_data(workspace_details)
                all_details.append(workspace_details.get("attributes"))
            links = response.json().get("links").get("next")
            if links is None:
                break
            url = f"{self.base_url}{links}"
        return all_details

    def _modify_data(self, data):
        """
        Removing less informative fields and making information user friendly
        """
        data_dict = data.get("attributes")
        if "project_property" in data_dict:
            del data_dict["project_property"]
        if "active" in data_dict:
            del data_dict["active"]
        if "created_time" in data_dict:
            del data_dict["created_time"]
        if "creator" in data_dict:
            del data_dict["creator"]
        if "organisation" in data_dict:
            del data_dict["organisation"]
        if "last_modified" in data_dict:
            data_dict["last_modified"] = data_dict["last_modified"].split(".")[0]
        if "status" in data_dict:
            if data_dict["status"] == 1:
                data_dict["status"] = "active"
            else:
                data_dict["status"] = "archived"

    @Track.track_decorator
    def list_contents(self, workspace_id: str):
        """
        This function fetches contents of a workspace from Polly.

        ``Args:``
            |  ``workspace_id :`` workspace id for the target workspace.

        ``Returns:``
            |  it will return a table with attributes.


        .. code::


                # create a obj
                workspaces = Workspaces(token)
                # from there you can other methods
                workspaces.list_contents(workspace_id)
        """
        url = f"{self.base_url}/projects/{workspace_id}/files"
        response = self.session.get(url)
        error_handler(response)
        details_list = []
        data = response.json()["data"]
        columns = ["file_name", "size", "last_modified"]
        for i in data:
            entry_list = []
            file_name = i.get("attributes").get(columns[0])
            size = i.get("attributes").get(columns[1])
            last_modified = i.get("attributes").get(columns[2])
            entry_list.append(file_name)
            entry_list.append(size)
            entry_list.append(last_modified)
            details_list.append(entry_list)
        df = pd.DataFrame(details_list, columns=columns)
        return df

    @Track.track_decorator
    def create_copy(
        self, source_id: int, source_path: str, destination_id: int, destination_path=""
    ) -> None:
        """
        Function to create a copy of files/folders existing in a workspace into another workspace.
        Args:
              source_id (int): workspace id of the source workspace where the file/folder exists
              source_path (str) : file/folder path on the source workspace to be copied
              destination_id (int) : workspace id of the destination workspace where the file/folder is to be copied
              destination_path (str, optional) : optional parameter to specify the destination path

        Raises:
              InvalidParameterException: when the parameter like source id is invalid
              InvalidPathException: when the source path is invalid
        """
        if not (source_id and isinstance(source_id, int)):
            raise InvalidParameterException("source_id")
        if not (destination_id and isinstance(destination_id, int)):
            raise InvalidParameterException("destination_id")
        if not (source_path and isinstance(source_path, str)):
            raise InvalidParameterException("source_path")
        url = f"{self.base_url}/projects/{destination_id}/files/{destination_path}"
        source_key = f"{source_id}/{source_path}"
        params = {"source": "workspace"}
        sts_url = f"{self.base_url}/projects/{source_id}/credentials/files"
        creds = self.session.get(sts_url)
        error_handler(creds)
        credentials = helpers.get_sts_creds(creds.json())
        bucket = f"mithoo-{self.env_string}-project-data-v1"
        s3_path = f"{bucket}/{source_id}/"
        s3_path = f"s3://{helpers.make_path(s3_path, source_path)}"
        payload = helpers.get_workspace_payload(
            s3_path, credentials, source_key, source_path
        )
        response = self.session.post(url, data=json.dumps(payload), params=params)
        error_handler(response)
        message = response.json()["data"][0].get("attributes", {}).get("body")
        print(message)
        links = response.json().get("included")[0].get("links")
        url = f"{self.base_url}{links.get('self')}"
        while True:
            response = self.session.get(url)
            error_handler(response)
            status = response.json().get("data").get("status")
            if status != "INITIATED":
                break
        print("Copy Operation Successful!")

    @Track.track_decorator
    def upload_to_workspaces(
        self, workspace_id: int, workspace_path: str, local_path: str
    ) -> None:
        """
        Function to upload files/folders to workspaces.
        Args:
              workspace_id (int) : id of the workspace where file need to uploaded
              workspace_path (str) : path where the file is to be uploaded.
              Creates the folder if provided folder path doesn't exist.
              local_path (str) : uploaded file path

        Raises:
              InvalidParameterException: when the parameter like workspace id is invalid
              InvalidPathException: when the file to path is invalid

        """
        if not (workspace_id and isinstance(workspace_id, int)):
            raise InvalidParameterException("workspace_id")
        if not (local_path and isinstance(local_path, str)):
            raise InvalidParameterException("local_path")
        if not (workspace_path and isinstance(workspace_path, str)):
            raise InvalidParameterException("workspace_path")
        isExists = os.path.exists(local_path)
        if not isExists:
            raise InvalidPathException
        # check for access rights for the workspace_id
        access_workspace = helpers.workspaces_permission_check(self, workspace_id)
        if not access_workspace:
            raise AccessDeniedError(
                detail=f"Access denied to workspace-id - {workspace_id}"
            )
        sts_url = f"{self.base_url}/projects/{workspace_id}/credentials/files"
        creds = self.session.get(sts_url)
        error_handler(creds)
        credentials = helpers.get_sts_creds(creds.json())
        bucket = f"mithoo-{self.env_string}-project-data-v1"
        s3_path = f"{bucket}/{workspace_id}/"
        s3_path = f"s3://{helpers.make_path(s3_path, workspace_path)}"
        helpers.upload_to_S3(s3_path, local_path, credentials)
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Upload successful on workspace-id={workspace_id}.")

    @Track.track_decorator
    def download_from_workspaces(self, workspace_id: int, workspace_path: str) -> None:
        """
        Function to download files/folders from workspaces.
        A message will be displayed on the status of the operation.
        Args:
              workspace_id (int) : Id of the workspace where file needs to uploaded
              workspace_path (str) : Downloaded file on workspace
        Returns:
              None
        Raises:
              InvalidPathException : Invalid file path provided
              OperationFailedException : Failed download
              InvalidParameterException : Invalid parameter passed
        """
        if not (workspace_id and isinstance(workspace_id, int)):
            raise InvalidParameterException("workspace_id")
        if not (workspace_path and isinstance(workspace_path, str)):
            raise InvalidParameterException("workspace_path")
        # check for access rights for the workspace_id
        access_workspace = helpers.workspaces_permission_check(self, workspace_id)
        if not access_workspace:
            raise AccessDeniedError(
                detail=f"Access denied to workspace-id - {workspace_id}"
            )
        sts_url = f"{self.base_url}/projects/{workspace_id}/credentials/files"
        creds = self.session.get(sts_url)
        error_handler(creds)
        credentials = helpers.get_sts_creds(creds.json())
        bucket = f"mithoo-{self.env_string}-project-data-v1"
        s3_path = f"{bucket}/{workspace_id}/"
        s3_path = f"s3://{helpers.make_path(s3_path, workspace_path)}"
        helpers.download_from_S3(s3_path, workspace_path, credentials)
