## Install:
    pip install selenium

## About SameSite Cookies
SameSite cookies are a security feature introduced in Chrome 80 and Firefox 69 to help prevent cross-site request forgery (CSRF) attacks. These cookies specify whether a cookie should be sent to the server only when the origin of the request is the same as the origin of the cookie.

**Types of SameSite Cookies:**

*Strict:* The cookie is sent only when the request is from the same origin as the cookie. This is the most restrictive setting and can prevent CSRF attacks effectively.

*Lax:* The cookie is sent to the server only when the request is from the same origin as the cookie or from a top-level navigation (e.g., clicking a link or typing a URL in the address bar). This setting is less restrictive than "Strict" but still helps prevent many CSRF attacks.

*None:* The cookie is sent to the server regardless of the origin of the request. This setting is the least restrictive and can potentially allow CSRF attacks if not used carefully.
Implications of SameSite Cookies:









