# About
Office365 REST API client for Python

The list of supported Office 365 REST APIs:

-   [SharePoint REST API](https://msdn.microsoft.com/en-us/library/office/jj860569.aspx) (_supported_ versions: [SharePoint 2013](https://msdn.microsoft.com/library/office/jj860569(v=office.15).aspx), SharePoint 2016, SharePoint Online and OneDrive for Business)
-   [Outlook REST API](https://msdn.microsoft.com/en-us/office/office365/api/use-outlook-rest-api#DefineOutlookRESTAPI)
    -   [Outlook Contacts REST API](https://msdn.microsoft.com/en-us/office/office365/api/contacts-rest-operations)
    -   [Outlook Calendar REST API](https://msdn.microsoft.com/en-us/office/office365/api/calendar-rest-operations)
    -   [Outlook Mail REST API](https://msdn.microsoft.com/en-us/office/office365/api/mail-rest-operations)


# Installation

Use pip3:
```
pip3 install git+https://github.com/rognick/cmdline-sharepoint.git
```

Use python3:

Clone repo an run
```
python3 setup.py install
```


# Usage: working with SharePoint resources

Run in terminal:
```
usage: cmdline_sharepoint [-h] -u USER -f FILE -d ABSOLUTE_URL
```

optional arguments:
```
  -h, --help            show this help message and exit
  -u USER, --user USER  username:password for login in SharePoint
  -f FILE, --upload_file FILE
                        File path to be uploaded
  -d ABSOLUTE_URL, --absolute_url ABSOLUTE_URL
                        An absolute URL defines the exact location of the
                        folder in SharePoint
```

# Python Version
Python 3 is fully supported.


# Third Party Libraries and Dependencies
The following libraries will be installed when you install the client library:
* [requests](https://github.com/kennethreitz/requests)
