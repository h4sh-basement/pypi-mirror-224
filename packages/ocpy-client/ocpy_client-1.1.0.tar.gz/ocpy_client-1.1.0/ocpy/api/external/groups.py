import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint

from typing import List

from ocpy.api.api_client import OpenCastBaseApiClient


class Group:
    def __init__(self, user, password, url, data):
        self.base_url = url
        self.user = user
        self.password = password
        self.data = data

    def __str__(self):
        return json.dumps(self.data, sort_keys=True, indent=4, separators=(",", ": "))

    def __repr__(self):
        return self.__str__()

    def get_identifier(self) -> str:
        return self.data["identifier"]

    def get_role(self) -> str:
        return self.data["role"]

    def get_organization(self) -> List[str]:
        return self.data["organization"]

    def get_roles(self) -> str:
        return self.data["roles"]

    def get_members(self) -> str:
        return self.data["members"]

    def get_name(self) -> str:
        return self.data["name"]

    def get_description(self) -> str:
        return self.data["description"]

    def add_member(self, username: str, **kwargs):
        res = requests.post(
            self.base_url + "/members",
            auth=HTTPBasicAuth(self.user, self.password),
            data={"member": username},
            **kwargs
        )
        if res.ok:
            return res.content
        return False

    def remove_member(self, username: str, **kwargs):
        res = requests.delete(
            self.base_url + "/members/" + username,
            auth=HTTPBasicAuth(self.user, self.password),
            **kwargs
        )
        return res.ok

    def update_group(
        self,
        name: str = None,
        description: str = None,
        roles: str = None,
        members: str = None,
        **kwargs
    ):
        if name is None:
            name = self.data["name"]
        res = requests.put(
            self.base_url,
            auth=HTTPBasicAuth(self.user, self.password),
            data={
                "name": name,
                "description": description,
                "roles": roles,
                "members": members,
            },
            **kwargs
        )
        return res.ok

    def delete(self, **kwargs):
        res = requests.delete(
            self.base_url, auth=HTTPBasicAuth(self.user, self.password), **kwargs
        )
        return res.ok


class GroupsApi(OpenCastBaseApiClient):
    def __init__(self, user=None, password=None, server_url=None, **kwargs):
        super().__init__(user, password, server_url)
        self.base_url = self.server_url + "/api/groups/"

    def get_groups(self, limit=100, offset=0, **kwargs) -> List[Group]:
        """
        :param limit:
        :param offset:
        :param kwargs:
        :return: List[Series]
        """
        parameters = {"limit": limit, "offset": offset}
        results = []
        res = requests.get(
            self.base_url,
            auth=HTTPBasicAuth(self.user, self.password),
            params=parameters,
            **kwargs
        )
        if res.ok:
            for g in res.json():
                results.append(
                    Group(self.user, self.password, self.base_url + g["identifier"], g)
                )
        return results

    def get_all_groups(self) -> List[Group]:
        result = []
        while True:
            res = self.get_groups(limit=100, offset=len(result))
            if res is None or len(res) <= 0:
                break
            result.extend(res)
        return result

    def create_group(
        self,
        name: str,
        description: str = None,
        roles: str = None,
        members: str = None,
        **kwargs
    ):
        res = requests.post(
            self.base_url,
            auth=HTTPBasicAuth(self.user, self.password),
            data={
                "name": name,
                "description": description,
                "roles": roles,
                "members": members,
            },
            **kwargs
        )
        return res.ok

    def get_group(self, identifier, **kwargs):
        res = requests.get(
            self.base_url + identifier,
            auth=HTTPBasicAuth(self.user, self.password),
            **kwargs
        )
        g = res.json()
        return Group(self.user, self.password, self.base_url + g["identifier"], g)


def main():
    api = GroupsApi()
    groups = api.get_groups()
    pprint(groups)
    for g in groups:
        print(g)
        if g.get_name() == "tests":
            print("tests")
            print(g.update_group(description="tolle gruppe die iae"))
            print(api.get_group(g.get_identifier()))
            print(g.add_member("depp"))
            print(g.remove_member("depp"))
            # print(g.delete())

    print(api.create_group("tests"))


if __name__ == "__main__":
    main()
