%define name	pythia
%define major	8
%define minor	1
%define version	%{major}.%{minor}
%define release	%mkrel 3

%define devname	%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Physics
License:	GPLv2
Version:	%{version}
Release:	%{release}
Summary:	High-energy pp and pbarp collisions simulation
URL:		http://home.thep.lu.se/~torbjorn/Pythia.html
Source0:	http://home.thep.lu.se/~torbjorn/pythia8/pythia8130.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	hepmc-devel

%description
Pythia 8 release is focussed towards LHC and Tevatron applications, i.e.
high-energy pp and pbarp collisions. Also e+e- and mu+mu- annihilation
processes may be simulated, but not e.g. ep, gammap or gammagamma collisions. 


#------------------------------------------------------------------------
%package	-n %{devname}
Summary:	Pythia runtime and development files
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{devname}
Pythia runtime and development files.


#------------------------------------------------------------------------
%prep
%setup -q -n pythia8130


#------------------------------------------------------------------------
%build
./configure --enable-shared --with-hepmc=%{_prefix}
%make


#------------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_libdir}
cp -fa lib/*.so lib/archive/*.a %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fa include/[A-Z]*.h %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -fa AUTHORS GUIDELINES examples htmldoc phpdoc xmldoc worksheet.pdf %{buildroot}%{_datadir}/%{name}


#------------------------------------------------------------------------
%clean
rm -fr %{buildroot}


#------------------------------------------------------------------------
%files		-n %{devname}
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_includedir}/%{name}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
