#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pexpect
Version  : 4.8.0
Release  : 79
URL      : https://files.pythonhosted.org/packages/e5/9b/ff402e0e930e70467a7178abb7c128709a30dfb22d8777c043e501bc1b10/pexpect-4.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/9b/ff402e0e930e70467a7178abb7c128709a30dfb22d8777c043e501bc1b10/pexpect-4.8.0.tar.gz
Summary  : Pexpect allows easy control of interactive console applications.
Group    : Development/Tools
License  : ISC
Requires: pypi-pexpect-license = %{version}-%{release}
Requires: pypi-pexpect-python = %{version}-%{release}
Requires: pypi-pexpect-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ptyprocess)

%description
Pexpect is a pure Python module for spawning child applications; controlling
        them; and responding to expected patterns in their output. Pexpect works like
        Don Libes' Expect. Pexpect allows your script to spawn a child application and
        control it as if a human were typing commands.
        
        Pexpect can be used for automating interactive applications such as ssh, ftp,
        passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
        software package installations on different servers. It can be used for
        automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
        Pexpect is pure Python.
        
        The main features of Pexpect require the pty module in the Python standard
        library, which is only available on Unix-like systems. Some features—waiting
        for patterns from file descriptors or subprocesses—are also available on
        Windows.

%package license
Summary: license components for the pypi-pexpect package.
Group: Default

%description license
license components for the pypi-pexpect package.


%package python
Summary: python components for the pypi-pexpect package.
Group: Default
Requires: pypi-pexpect-python3 = %{version}-%{release}

%description python
python components for the pypi-pexpect package.


%package python3
Summary: python3 components for the pypi-pexpect package.
Group: Default
Requires: python3-core
Provides: pypi(pexpect)
Requires: pypi(ptyprocess)

%description python3
python3 components for the pypi-pexpect package.


%prep
%setup -q -n pexpect-4.8.0
cd %{_builddir}/pexpect-4.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650914953
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pexpect
cp %{_builddir}/pexpect-4.8.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pexpect/5a99e7077ee89ba92fb3f584855e8970096cd5dc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pexpect/5a99e7077ee89ba92fb3f584855e8970096cd5dc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
