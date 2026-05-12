; LegalKit Lite EN v7.47 - Inno Setup
; CPU INT8 mode, works on any Windows 10/11 PC (no GPU required)

#define AppName "LegalKit Lite EN"
#define AppVersion "7.47"
#define AppPublisher "Vibe Toolsmith"
#define AppExeName "LegalKit_EN.exe"

[Setup]
AppId={{LEGALKIT-LITE-EN-7-0-4}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\LegalKit\Lite_EN
DefaultGroupName=LegalKit Lite
OutputDir=installer_out
OutputBaseFilename=LegalKit_Lite_EN_v7.47_setup
Compression=lzma2/ultra
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableProgramGroupPage=yes
WizardStyle=modern

[Languages]
Name: "default"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "payload_lite_EN\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\LegalKit Lite EN"; Filename: "{app}\{#AppExeName}"
Name: "{commondesktop}\LegalKit Lite EN"; Filename: "{app}\{#AppExeName}"

[Run]
Filename: "{app}\{#AppExeName}"; Description: "Launch LegalKit Lite EN"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{userappdata}\VibeToolsmith\LegalKit"
