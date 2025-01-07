from ...SotiApiClient import SotiApiClient


# Returns all MobiControl console users or those that match the provided search criteria. Hidden users are users implicitly authorized to login to MobiControl through an LDAP group and have logged in at least once.
# searchString: The search string to filter the users

async def search_for_user(client:SotiApiClient, searchString:str, includeHiddenUsers:bool, kind:str):
    # Validate that kind is either LdapUser, SsoUser or MobiControlUser
    if kind not in ['LdapUser', 'SsoUser', 'MobiControlUser']:
        raise ValueError('kind must be either LdapUser, SsoUser or MobiControlUser')
                         
    endpoint = f"/security/users?searchString={searchString}&includeHiddenUsers={includeHiddenUsers}&kind={kind}"
    return await client.get_data(endpoint)