class Config:

    class GENERIC:

        SUCCESS                 = (0, "Success")
        FAILURE                 = (1, "Oops something went wrong. We have noted this error and will get it fixed soon")
        BAD_REQUEST             = (2, "Bad Request")
        WRONG_CREDENTIALS       = (3, "Wrong Credentials")
        DOES_NOT_EXIST          = (4, "Not found")
        NOT_AUTHORISED          = (5, "Not Authorized")
        INCOMPLETE_HEADERS      = (6, "Please provide all the headers")
        NO_CONTENT              = (7, "No content")
        INTEGRITY_ERROR         = (8, "Integrity error")
        FORBIDDEN               = (9, "Forbidden")
        BODY_NOT_MAP            = (10, "Body is not a valid JSON map")
        OPERATOR_ALREADY_LINK   = (11,"Cannot generate OTP for FSE mobile number")
        MOA_APP_VERSION         = (13, "This version in deprecated, Please connect with park+ support team.")
        WRONG_ROLE_NAME           = (14, "Wrong role name please do check")
        LOGGED_OUT              = (0, "Successfully logged out the user !")
        # UPSTREAM_REQUEST_TIMEOUT= (11,"Request time out from upstream")
        OPERATION_NOT_ALLOWED   = (17, "Either role id is wrong or operation not allowed on this role id")

    class USER:
        TITLE                   = (1, "Title is missing")
        DESCRIPTION             = (2, "description is missing")
        AUTHOR                  = (3, "Author is missing")

    class URLS:
        BASE_URL =   "http://127.0.0.1:8000/get/{id}"

