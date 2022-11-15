Name:		texlive-chklref
Version:	52649
Release:	1
Summary:	Check for problems with labels in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chklref
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chklref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chklref.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
It is quite common that after modifying a TeX file, many unused
labels remain in it. The purpose of chklref is to automatically
find these useless labels. It also looks for "non starred"
mathematical environments with no labels and advises the user
to use a starred version instead.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/tex/latex/chklref
%{_texmfdistdir}/scripts/chklref
%doc %{_texmfdistdir}/doc/support/chklref
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
