; LegalKit Lite KR v7.47 - Inno Setup
; CPU INT8 mode, works on any Windows 10/11 PC (no GPU required)

#define AppName "LegalKit Lite KR"
#define AppVersion "7.47"
#define AppPublisher "Vibe Toolsmith"
#define AppExeName "LegalKit_KR.exe"

[Setup]
AppId={{LEGALKIT-LITE-KR-7-0-4}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\LegalKit\Lite_KR
DefaultGroupName=LegalKit Lite
OutputDir=installer_out
OutputBaseFilename=LegalKit_Lite_KR_v7.47_setup
Compression=lzma2/ultra
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableProgramGroupPage=yes
WizardStyle=modern

[Languages]
Name: "default"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "payload_lite_KR\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\LegalKit Lite KR"; Filename: "{app}\{#AppExeName}"
Name: "{commondesktop}\LegalKit Lite KR"; Filename: "{app}\{#AppExeName}"

[Run]
Filename: "{app}\{#AppExeName}"; Description: "Launch LegalKit Lite KR"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{userappdata}\VibeToolsmith\LegalKit"
