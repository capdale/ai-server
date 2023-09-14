function Complie-Proto {
    param (
        $Filepath
    )
    python.exe -m grpc_tools.protoc -I ./proto --python_out=./proto --grpc_python_out=./proto --pyi_out=./proto $Filepath
}

function Check-Package {
    param (
        $PackageName
    )
    $result = python.exe -m pip list | Select-String -Pattern $PackageName
    Write-Output $result
    if ($null -eq $result) {
        return $false
    }
    return $true
}

function Install-Package {
    param (
        $PackageName
    )
    python.exe -m pip install $PackageName
}

$PreRequirements = @(
    "grpcio"
    "grpcio-tools"
)

foreach ($packageName in $PreRequirements) {
    if (!(Check-Package $packageName)) {
        Install-Package $packageName
    }
}

foreach ($arg in $args) {
    Complie-Proto $arg
}