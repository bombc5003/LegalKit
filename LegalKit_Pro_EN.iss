; LegalKit Pro EN v7.47 Inno Setup script
; NVIDIA cuBLAS+cuDNN bundled. GPU-accelerated transcription (RTX-class required).

#define AppName "LegalKit Pro EN"
#define AppVersion "7.47"
#define AppPublisher "Vibe Toolsmith"
#define AppExeName "LegalKit_EN.exe"

[Setup]
AppId={{LEGALKIT-PRO-EN-7-0-8}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\LegalKit\Pro_EN
DefaultGroupName=LegalKit Pro
OutputDir=installer_out
OutputBaseFilename=LegalKit_Pro_EN_v7.47_setup
Compression=lzma2/normal
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableProgramGroupPage=yes
WizardStyle=modern

[Languages]
Name: "default"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist_pro\LegalKit_EN\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\LegalKit Pro EN"; Filename: "{app}\{#AppExeName}"
Name: "{commondesktop}\LegalKit Pro EN"; Filename: "{app}\{#AppExeName}"

[Run]
Filename: "{app}\{#AppExeName}"; Description: "Launch LegalKit Pro EN"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{userappdata}\VibeToolsmith\LegalKit"
