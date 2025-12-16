#!/usr/bin/env python3
"""
Convert Factory Method markdown to PDF
"""

import subprocess
import os

md_file = "/Users/aayushtarwey/python_design_pattern/creational_patterns/factory_method/docs/FACTORY_METHOD_GUIDE.md"
pdf_file = "/Users/aayushtarwey/python_design_pattern/creational_patterns/factory_method/docs/FACTORY_METHOD_GUIDE.pdf"

# Read the markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Convert markdown to HTML with styling
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factory Method Pattern - Complete Learning Guide</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 40px 20px;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #2c3e50;
            font-size: 2.5em;
            margin-top: 0.5em;
            margin-bottom: 0.5em;
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 15px;
        }}
        
        h2 {{
            color: #2c3e50;
            font-size: 1.8em;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 8px;
        }}
        
        h3 {{
            color: #34495e;
            font-size: 1.3em;
            margin-top: 1.2em;
            margin-bottom: 0.5em;
        }}
        
        h4, h5, h6 {{
            color: #34495e;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }}
        
        p {{
            margin-bottom: 1em;
        }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: 0.95em;
            color: #c7254e;
        }}
        
        pre {{
            background-color: #282c34;
            color: #abb2bf;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #e74c3c;
            overflow-x: auto;
            margin: 15px 0;
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: 0.9em;
            line-height: 1.4;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
            color: #abb2bf;
            border: none;
        }}
        
        blockquote {{
            border-left: 4px solid #e74c3c;
            padding-left: 15px;
            margin-left: 0;
            color: #666;
            font-style: italic;
            background-color: #f9f9f9;
            padding: 10px 15px;
            margin: 15px 0;
        }}
        
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 8px 0;
        }}
        
        a {{
            color: #e74c3c;
            text-decoration: none;
            border-bottom: 1px solid #e74c3c;
        }}
        
        a:hover {{
            background-color: #ecf0f1;
        }}
        
        strong {{
            font-weight: 600;
            color: #2c3e50;
        }}
        
        em {{
            font-style: italic;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            border: 1px solid #ddd;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #e74c3c;
            color: white;
            font-weight: 600;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        
        .highlight {{
            background-color: #fff3cd;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        
        @media print {{
            body {{
                background-color: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 0;
                max-width: 100%;
            }}
            
            a {{
                border-bottom: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

try:
    # Using Chrome's headless mode to convert HTML to PDF
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium"
    ]
    
    chrome_path = None
    for path in chrome_paths:
        if os.path.exists(path):
            chrome_path = path
            break
    
    if chrome_path:
        command = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={pdf_file}",
            f"file:///tmp/factory_method_temp.html"
        ]
        
        # Write temporary HTML file
        with open('/tmp/factory_method_temp.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Update command to use temp file
        command[-1] = f"file:///tmp/factory_method_temp.html"
        
        print("Converting Factory Method documentation to PDF...")
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        if os.path.exists(pdf_file):
            print(f"✅ PDF created successfully!")
            print(f"📄 Location: {pdf_file}")
            print(f"📊 File size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
        else:
            raise Exception("PDF file was not created")
    else:
        raise Exception("Chrome/Chromium not found")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nNote: You can manually create PDF:")
    print("1. Open the markdown file in your browser")
    print("2. Print to PDF (Cmd+P)")
