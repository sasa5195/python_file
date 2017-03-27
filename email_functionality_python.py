Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 152, in __init__
    self._imap = self._create_IMAP4()
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 164, in _create_IMAP4
    self._timeout)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 171, in __init__
    imaplib.IMAP4.__init__(self, host, port)
  File "C:\Python27\lib\imaplib.py", line 173, in __init__
    self.open(host, port)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 177, in open
    self.sock = wrap_socket(sock, self.ssl_context, host)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 144, in wrap_socket
    ssl_context = create_default_context()
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 127, in create_default_context
    context.load_verify_locations(cadata=certs)
  File "C:\Python27\lib\site-packages\backports\ssl\core.py", line 654, in load_verify_locations
    self._ctx.load_verify_locations(cafile, capath)
  File "C:\Python27\lib\site-packages\OpenSSL\SSL.py", line 525, in load_verify_locations
    _raise_current_error()
  File "C:\Python27\lib\site-packages\OpenSSL\_util.py", line 48, in exception_from_error_queue
    raise exception_type(errors)
Error: []
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 152, in __init__
    self._imap = self._create_IMAP4()
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 164, in _create_IMAP4
    self._timeout)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 171, in __init__
    imaplib.IMAP4.__init__(self, host, port)
  File "C:\Python27\lib\imaplib.py", line 173, in __init__
    self.open(host, port)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 177, in open
    self.sock = wrap_socket(sock, self.ssl_context, host)
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 144, in wrap_socket
    ssl_context = create_default_context()
  File "C:\Python27\lib\site-packages\imapclient\tls.py", line 127, in create_default_context
    context.load_verify_locations(cadata=certs)
  File "C:\Python27\lib\site-packages\backports\ssl\core.py", line 654, in load_verify_locations
    self._ctx.load_verify_locations(cafile, capath)
  File "C:\Python27\lib\site-packages\OpenSSL\SSL.py", line 525, in load_verify_locations
    _raise_current_error()
  File "C:\Python27\lib\site-packages\OpenSSL\_util.py", line 48, in exception_from_error_queue
    raise exception_type(errors)
Error: []
>>> imapclient.__version__
u'1.0.2'
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True,ssl_context=context)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True,ssl_context=context)
NameError: name 'context' is not defined
>>> context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
NameError: name 'ssl' is not defined
>>> from backports import ssl
>>> context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True,ssl_context=context)
>>> imapObj.login(' baidsahil@gmail.com ', ' sahil5195 ')

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    imapObj.login(' baidsahil@gmail.com ', ' sahil5195 ')
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 215, in login
    unpack=True,
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 1180, in _command_and_check
    typ, data = meth(*args)
  File "C:\Python27\lib\imaplib.py", line 520, in login
    raise self.error(dat[-1])
error: [ALERT] Please log in via your web browser: https://support.google.com/mail/accounts/answer/78754 (Failure)
>>> imapObj.login(' baidsahil@gmail.com ', ' sahil5195 ')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    imapObj.login(' baidsahil@gmail.com ', ' sahil5195 ')
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 215, in login
    unpack=True,
  File "C:\Python27\lib\site-packages\imapclient\imapclient.py", line 1180, in _command_and_check
    typ, data = meth(*args)
  File "C:\Python27\lib\imaplib.py", line 520, in login
    raise self.error(dat[-1])
error: [ALERT] Please log in via your web browser: https://support.google.com/mail/accounts/answer/78754 (Failure)
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True,ssl_context=context)
>>> imapObj.login(' baidsahil@gmail.com ', ' sahil5195 ')
'baidsahil@gmail.com authenticated (Success)'
>>> import pprint
>>> pprint.pprint(imapObj.list_folders())
[(('\\HasNoChildren',), '/', u'FAMILY'),
 (('\\HasNoChildren',), '/', u'INBOX'),
 (('\\HasNoChildren',), '/', u'IPUSC'),
 (('\\HasNoChildren',), '/', u'Personal'),
 (('\\HasNoChildren',), '/', u'Receipts'),
 (('\\HasNoChildren',), '/', u'SAT'),
 (('\\HasNoChildren',), '/', u'Sent'),
 (('\\HasNoChildren',), '/', u'Trash'),
 (('\\HasNoChildren',), '/', u'Travel'),
 (('\\HasNoChildren',), '/', u'Work'),
 (('\\HasChildren', '\\Noselect'), '/', u'[Gmail]'),
 (('\\All', '\\HasNoChildren'), '/', u'[Gmail]/All Mail'),
 (('\\Drafts', '\\HasNoChildren'), '/', u'[Gmail]/Drafts'),
 (('\\HasNoChildren', '\\Important'), '/', u'[Gmail]/Important'),
 (('\\HasNoChildren', '\\Sent'), '/', u'[Gmail]/Sent Mail'),
 (('\\HasNoChildren', '\\Junk'), '/', u'[Gmail]/Spam'),
 (('\\Flagged', '\\HasNoChildren'), '/', u'[Gmail]/Starred'),
 (('\\HasNoChildren', '\\Trash'), '/', u'[Gmail]/Trash')]
>>> 
KeyboardInterrupt
>>> imapObj.logout()
'LOGOUT Requested'
>>> 
