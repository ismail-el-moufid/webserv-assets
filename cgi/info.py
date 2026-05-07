#!/usr/bin/env python3
"""
info.py - CGI script that displays server and environment information.
"""

import cgi
import cgitb
import os
import sys
import platform
import datetime

# Enable detailed error tracebacks in the browser
cgitb.enable()

def html_row(label, value):
    return f"""
        <tr>
            <td class="label">{cgi.escape(str(label)) if hasattr(cgi, 'escape') else label}</td>
            <td class="value">{str(value)}</td>
        </tr>"""

def get_env_rows():
    rows = ""
    for key in sorted(os.environ):
        rows += html_row(key, os.environ[key])
    return rows

def main():
    print("Content-Type: text/html; charset=utf-8")
    print()  # Blank line required between headers and body

    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python CGI Info</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f0f2f5;
            color: #333;
            padding: 30px 20px;
        }}
        h1 {{
            font-size: 1.8rem;
            color: #2c3e50;
            margin-bottom: 6px;
        }}
        .subtitle {{
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 30px;
        }}
        .card {{
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 24px;
            overflow: hidden;
        }}
        .card-header {{
            background: #3498db;
            color: #fff;
            padding: 12px 20px;
            font-weight: 600;
            font-size: 1rem;
            letter-spacing: 0.5px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        tr:nth-child(even) {{ background: #f8f9fa; }}
        td {{
            padding: 9px 20px;
            font-size: 0.875rem;
            border-bottom: 1px solid #eee;
            vertical-align: top;
            word-break: break-all;
        }}
        td.label {{
            font-weight: 600;
            color: #555;
            width: 35%;
            white-space: nowrap;
        }}
        td.value {{ color: #222; }}
    </style>
</head>
<body>
    <h1>🐍 Python CGI Info</h1>
    <p class="subtitle">Generated on {now}</p>

    <!-- Python & System Info -->
    <div class="card">
        <div class="card-header">Python &amp; System</div>
        <table>
            {html_row("Python Version", sys.version)}
            {html_row("Platform", platform.platform())}
            {html_row("Architecture", " / ".join(platform.architecture()))}
            {html_row("Hostname", platform.node())}
            {html_row("Processor", platform.processor() or "N/A")}
            {html_row("Script Path", os.path.abspath(__file__))}
            {html_row("Working Directory", os.getcwd())}
            {html_row("Server Time (UTC)", now)}
        </table>
    </div>

    <!-- CGI / Request Info -->
    <div class="card">
        <div class="card-header">CGI / Request</div>
        <table>
            {html_row("Request Method", os.environ.get("REQUEST_METHOD", "N/A"))}
            {html_row("Script Name", os.environ.get("SCRIPT_NAME", "N/A"))}
            {html_row("Query String", os.environ.get("QUERY_STRING", "(empty)"))}
            {html_row("Remote Address", os.environ.get("REMOTE_ADDR", "N/A"))}
            {html_row("Remote Host", os.environ.get("REMOTE_HOST", "N/A"))}
            {html_row("HTTP Host", os.environ.get("HTTP_HOST", "N/A"))}
            {html_row("HTTP User-Agent", os.environ.get("HTTP_USER_AGENT", "N/A"))}
            {html_row("Content Type", os.environ.get("CONTENT_TYPE", "N/A"))}
            {html_row("Content Length", os.environ.get("CONTENT_LENGTH", "N/A"))}
            {html_row("Server Software", os.environ.get("SERVER_SOFTWARE", "N/A"))}
            {html_row("Server Protocol", os.environ.get("SERVER_PROTOCOL", "N/A"))}
            {html_row("Gateway Interface", os.environ.get("GATEWAY_INTERFACE", "N/A"))}
        </table>
    </div>

    <!-- All Environment Variables -->
    <div class="card">
        <div class="card-header">Environment Variables</div>
        <table>
            {get_env_rows()}
        </table>
    </div>

</body>
</html>
""")

if __name__ == "__main__":
    main()
