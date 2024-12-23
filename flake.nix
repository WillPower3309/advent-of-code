{
    description = "advent of code dev env";
    inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

    outputs = { self, nixpkgs }: 
    let
        supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
        forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
            pkgs = import nixpkgs { inherit system; };
        });
    in {
        devShells = forEachSupportedSystem ({pkgs}: {
            default = pkgs.mkShell {
                name = "advent-of-code-shell";
                venvDir = ".venv";
                packages = with pkgs; [ python312 ] ++ (with pkgs.python311Packages; [
                    pip
                    venvShellHook
                ]);
            };
        });
    };
}
