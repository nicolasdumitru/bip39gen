{
  description = "BIP39 mnemonic passphrase generator";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        bip39genPkg = pkgs.callPackage ./nix/package.nix { };
      in {
        # The default build output
        packages.default = bip39genPkg;

        # Allow `nix run .` to execute the CLI
        apps.default = flake-utils.lib.mkApp {
          drv = bip39genPkg;
          name = "bip39gen";
        };

        # Developer shell
        # devShells.default = pkgs.mkShell {
        #   buildInputs = [
        #     pkgs.python3
        #     pkgs.python3Packages.mnemonic
        #     pkgs.python3Packages.pytest
        #     pkgs.python3Packages.black
        #   ];
        # };
      });
}
