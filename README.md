# McAfeeWebGateway
Python-based API for interfacing with the McAfee Web Gateway REST API

This is a Python-based library for interfacing with McAfee's Web Gateway. Features include the following:

* Listing appliances
* Listing lists
* Viewing list entries
* Inserting into lists
* Saving data

This has been tested against 7.4 of the appliance and works with Python 2.7.

You will require the following Python libraries:

 * Requests
 * XMLtoDict
 * Dill (Pickle replacement)

The use of Dill is to combat any session exhaustions that may occur on the appliance.

## Usage

To import libraries, you can use the following:

    from mwg import *

To open and close a session:

    auth = authenticate(hostname='appliancehost')
    auth.createSession(username='yourusername', password='yourpassword')
    auth.destroySession()

To view lists:

    l = listdata(auth=auth.session, hostname=hostname)
    l.listData()

To view a specific list:

    l = listdata(auth=auth.session, hostname=hostname)
    l.listID(value='HostsToBlock')

To insert an item in a list (specifically to block):

    l.listIDInsert(value='HostsToBlock', entry='target.com', description='Blocking online shopping!')

And to save any changes after insertion:

    c = commit(auth=auth.session, hostname=hostname)
    c.commitData()

##Comments

In testing the McAfee Web Gateway's API is fairly slow but not as slow as the functions provided by the web application itself. Do expect that if you queue up any blocks that the actions to results may be a bit slower than you desire.