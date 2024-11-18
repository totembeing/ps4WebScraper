# ps4WebScraper

My initial code:

    webUrl = urllib.request.urlopen("https://www.bestbuy.ca/en-ca/category/ps4-games/33934")
    data = webUrl.read()
    print(data)

urllib.request.urlopen() function just sends a basic HTTP request without additional headers, like User-Agent.



Modern websites, like Best Buy in this case looks for a User-Agent header to determine if the request is coming from a legitimate browser or a bot. 

Since my initial code did not had a header in it, the request made by it was turned down by the website. The problem is solved with my updated code:

    url = "https://www.bestbuy.ca/en-ca/category/ps4-games/33934"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    webUrl = urllib.request.urlopen(req)

    data = webUrl.read()
    print(data)

In the updated code, since there is a header included, it imitates a request from a browser (e.g., Chrome) to which the website respond withe the appropriate content. Many servers use the absence of User-Agent to check for a bot-like request.

-> User-Agent is one of the request headers.
-> A header is a part of the metadata included in the request or response when a client and a server communicates.
-> HTTP headers provide additional information about request or response such as:
        - Who is making the request?
        - What type of data is being sent or expected 
        - How the client or the server should handle the data

-> There are two types of headers:
        - Request headers (sent by the client)
        - Response headers (sent by the server)

-> Request headers:
        - Provide context about the client or the request
        - Examples:
            + User-Agent: Identifies the client software (e.g., browser or Python script)
            + Accept: Specifies the type of data the client expects (e.g., text/html, application/json)
            + Authorization: Carries authentication details
            + Cookie: Sends cookies from the client to server

-> Response headers: 
        - Provide context about the server's response
        - Examples:
            + Content-Type: Indicates the type of data sent (e.g., text/html, application/json)
            + Set-Cookie: Instructs the client to store cookies
            + Server: Identifies the server software
    
-> User-Agent, a request header, provides the following information:
        - Browser name and version 
        - Operating system 
        - Rendering engine

        In the User-Agent used in this code: 
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36

        - Mozilla/5.0: Indicates compatibility with Mozilla-based browsers
        - Windows NT 10.0: Specifies the operating system 
        - Chrome/85.0.4183.121: Browser name and version
        - Safari/537.36: Rendering Engine 
            
-> req = urllib.request.Request(url, headers=headers)
        - urllib.request.Request is a class from urllib.request module that represents a HTTP request and provides a way to configure it
        - In this case we are creating a Request object (req), that stores all the information about the HTTP request (URL, header) 
        - headers=headers
            - headers on the left is the parameter needed for creating the Request object
            - headers on the right is the dictionary variable being assigned to the headers parameter

            