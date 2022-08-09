%global debug_package %{nil}

Name: packer-plugin-libvirt
Epoch: 100
Version: 0.2.0
Release: 1%{?dist}
Summary: Packer Plugin for Libvirt
License: MPL-2.0
URL: https://github.com/thomasklein94/packer-plugin-libvirt/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: golang-1.19
BuildRequires: glibc-static
Requires: packer

%description
The Libvirt multi-component plugin can be used with HashiCorp Packer to
create custom images.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
    export CGO_ENABLED=0 && \
    go build \
        -mod vendor -buildmode pie -v \
        -ldflags "-s -w -extldflags '-static -lm'" \
        -o ./packer-plugin-libvirt .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -t %{buildroot}%{_bindir}/ packer-plugin-libvirt

%files
%license LICENSE
%{_bindir}/*

%changelog
