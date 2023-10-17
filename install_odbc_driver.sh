if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

apt-get update 

export ACCEPT_EULA=Y 
apt-get install -y msodbcsql17

# optional: for bcp and sqlcmd
export ACCEPT_EULA=Y 
apt-get install -y mssql-tools17
echo 'export PATH="$PATH:/opt/mssql-tools17/bin"' >> ~/.bashrc
. ~/.bashrc
# optional: for unixODBC development headers
apt-get install -y unixodbc-dev