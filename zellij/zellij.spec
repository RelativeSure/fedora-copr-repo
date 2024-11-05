Name:       zellij
Version:    0.41.1
Release:    1%{?dist}
Summary:    A terminal workspace with batteries included.

License:    MIT
URL:        https://github.com/zellij-org/zellij
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: perl-devel
BuildRequires: openssl-perl
BuildRequires: perl-FindBin
BuildRequires: perl-IPC-Cmd

%description
%{summary}

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*

%changelog
%autochangelog