# McAfeeWebGateway
Python-based API for interfacing with the McAfee Web Gateway REST API

This is a Python-based library for interfacing with McAfee's Web Gateway. Features include the following:

* Listing appliances
* Listing lists
* Viewing list entries

This has been tested against 7.4 of the appliance and works with Python 2.7.

You will require the following Python libraries:

 * Requests
 * XMLtoDict
 * Dill (Pickle replacement)

The use of Dill is to combat any session exhaustions that may occur on the appliance.

## Usage

To open and close a session:

```from mwg import *
auth = authenticate(hostname='appliancehost')
auth.createSession(username='yourusername', password='yourpassword')
auth.destroySession()
```

To view lists:

```l = listdata(auth=auth.session, hostname=hostname)
l.listData()
```

To view a specific list:

```l = listdata(auth=auth.session, hostname=hostname)
l.listID(value='listnamehere')
```
