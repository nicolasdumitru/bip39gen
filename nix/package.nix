{ lib
, python3Packages
}:

python3Packages.buildPythonApplication rec {
  pname = "bip39gen";
  version = "1.0.0";
  format = "pyproject";
  src = ../.;

  # Add setuptools (and optionally wheel) as native build inputs
  nativeBuildInputs = with python3Packages; [
    setuptools
    wheel
    build  # optional but helps for PEP 517
  ];

  propagatedBuildInputs = with python3Packages; [
    mnemonic
  ];

  meta = with lib; {
    description = "Generate BIP39 mnemonic passphrases";
    homepage = "https://github.com/nicolasdumitru/bip39gen";
    license = licenses.gpl3Plus;
    # maintainers = [ ];
    platforms = platforms.all;
  };
}
