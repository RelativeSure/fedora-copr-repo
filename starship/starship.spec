%global debug_package %{nil}
%global github_org starship
# renovate: packageName=starship/starship

Name:       starship
Version:    1.21.1
Release:    1%{?dist}
Summary:    The minimal, blazing-fast, and infinitely customizable prompt for any shell!

License:    ISC
URL:        https://github.com/%{github_org}/%{name}
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%if 0%{?el8}
%else
BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
%endif
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
%autosetup -p1
%if 0%{?el8}
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif


%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
%if 0%{?el8}
  $HOME/.cargo/bin/cargo install --root=%{buildroot}%{_prefix} --path=.
%else
  cargo install --root=%{buildroot}%{_prefix} --path=.
%endif

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*


%files
#%license LICENSE.md
#%doc README.md
%{_bindir}/%{name}
