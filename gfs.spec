%define name gfs
%define version 6.1
%define pre cvs
%define release  %mkrel 2

Summary: gfs The Global File System
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-%pre.tar.bz2
License: GPL
Group: System
#Url: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: iddev gfs-kernel

%description
gfs The Global File System

%prep
%setup -q -n %{name}-%{version}-%pre

%build
./configure --incdir=%{_includedir} \
	--kernel_src=/usr/src/linux \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sbindir=%{_sbindir} \
	--sharedir=%{_datadir}/%name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT
mv -vf $RPM_BUILD_ROOT/etc/init.d/%name $RPM_BUILD_ROOT%{_initrddir}/%name

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/*
%doc
%{_mandir}
%{_initrddir}/%name

