# categories.py
# This file defines file categorizations for the organizer.
# You can edit this anytime without touching the main script.

file_cat = {
    # 🖼️ Image & Media Files
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico", ".heic"],  # Photos, icons, etc.
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm", ".m4v", ".3gp"],  # All video formats
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],  # Music and sound effects

    # 📄 Documents, Office & Text
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".wps"],  # General document types
    "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],  # Excel, LibreOffice Calc, data sheets
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],  # PowerPoint, Keynote, etc.
    "Ebooks": [".epub", ".mobi", ".azw3", ".djvu"],  # Digital books and readers
    "Notes": [".md", ".json", ".yaml", ".yml", ".xml"],  # Markdown, config, structured text

    # 💻 Development & Programming
    "Code": [".py", ".cpp", ".c", ".h", ".hpp", ".java", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".php", ".sql", ".rb", ".swift", ".go", ".rs", ".kt", ".sh", ".bat", ".ps1"],  # Source code files
    "Libraries": [".jar", ".dll", ".so", ".a", ".lib", ".pyd"],  # Shared and static libs
    "Configs": [".ini", ".env", ".toml", ".cfg", ".conf"],  # Config files for systems and projects
    "Scripts": [".vbs", ".lua", ".pl", ".r", ".m"],  # Scripting languages (batch, Lua, Perl, R, MATLAB)

    # 📦 Installers & Packages
    "Executables": [".exe", ".msi", ".apk", ".app", ".deb", ".rpm", ".pkg"],  # Application installers
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".xz", ".bz2", ".iso"],  # Archives & images

    # 🧮 Data & Analytics
    "Data": [".db", ".sqlite", ".sql", ".dbf", ".parquet", ".feather"],  # Databases & data formats
    "Logs": [".log"],  # Log files
    "Datasets": [".arff", ".sav", ".mat"],  # ML datasets or scientific formats
    "Pickles": [".pkl", ".joblib"],  # Serialized Python data files

    # 🧰 Design, Creative & Assets
    "Design": [".psd", ".ai", ".xd", ".fig", ".sketch", ".blend", ".max", ".c4d"],  # Design and 3D project files
    "Vectors": [".eps", ".pdf", ".ai", ".svg"],  # Vector graphics
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".fnt"],  # Font files
    "Textures": [".dds", ".tga", ".exr", ".hdr"],  # Game or render textures

    # 🎮 Games & Entertainment
    "GameFiles": [".pak", ".sav", ".dat", ".uasset", ".umap", ".rpf"],  # Game data files
    "Emulation": [".iso", ".bin", ".cue", ".n64", ".sfc", ".gba", ".nds", ".rom"],  # Emulator ROMs and ISOs
    "Torrents": [".torrent"],  # BitTorrent metadata files

    # 🌐 Internet & Web
    "Web": [".html", ".htm", ".css", ".js", ".php", ".asp", ".aspx"],  # Web development files
    "Bookmarks": [".url", ".webloc", ".desktop"],  # Saved web shortcuts
    "Downloads": [".crdownload", ".part", ".tmp"],  # Incomplete downloads

    # 🔐 Security & Certificates
    "Keys": [".pem", ".crt", ".cer", ".key", ".pub"],  # Encryption keys and certificates
    "Hashes": [".sha256", ".sha1", ".md5"],  # Hash files

    # 🧾 Finance & Business
    "Finance": [".qfx", ".qif", ".ofx", ".gnucash", ".xlsx"],  # Accounting and transaction files
    "Invoices": [".inv", ".pdf"],  # Custom invoice storage (may overlap Documents)

    # ⚙️ System Files
    "System": [".sys", ".drv", ".bak", ".tmp", ".dmp"],  # System, backup, and dump files

    # 🕹️ Miscellaneous
    "Shortcuts": [".lnk"],  # Windows shortcuts
    "CAD": [".dwg", ".dxf", ".stl"],  # Engineering design formats
    "GIS": [".shp", ".geojson", ".kml", ".kmz"],  # Geographic data formats

    # 🚀 Catch-all fallback
    "Others": []  # Anything uncategorized lands here
}