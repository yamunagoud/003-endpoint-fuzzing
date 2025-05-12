# 003-endpoint-fuzzing
a technique to test and discover API endpoints on a target server. It systematically checks multiple predefined endpoints by connecting via TCP sockets and analyzing responses.

Key Uses of the Code

✅ Security Testing – Helps uncover potential hidden endpoints that might not be documented. 

✅ API Enumeration – Useful for mapping available server paths before performing deeper security analysis. 

✅ Penetration Testing – Helps identify open endpoints that could be vulnerable to attacks like remote code execution (RCE). 

✅ Debugging & Reconnaissance – Can reveal error responses, misconfigurations, or unintended API exposures.

💡 Real-World Scenario: Suppose an attacker is testing a web application for security flaws. They might use this script to check for sensitive endpoints like:

http://target-ip:8000/admin

http://target-ip:8000/debug

http://target-ip:8000/shell

