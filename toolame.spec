Summary:	tooLAME - an optimized MPEG 1/2 layer 2 audio encoder
Summary(pl.UTF-8):	tooLAME - zoptymalizowany koder dźwięku MPEG 1/2 layer 2
Name:		toolame
Version:	0.2l
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/toolame/%{name}-%{fver}.tgz
# Source0-md5:	5946e2dd78fbb57e54386b3b5d873fee
# viewable with lynx only (due to non-closed table)
URL:		http://www.planckenergy.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tooLAME is an optimized MPEG Audio 1/2 Layer 2 encoder.

%description -l pl.UTF-8
tooLAME to zoptymalizowany koder dźwięku MPEG 1/2 layer 2.

%prep
%setup -q -n %{name}-%{fver}

%build
%{__make} \
	CC="%{__cc}" \
	OPTIM="%{rpmcflags}" \
	ARCH="" \
	PG="%{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install toolame $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# html/* have broken tables
%doc FUTURE HISTORY README text/*
%attr(755,root,root) %{_bindir}/*
