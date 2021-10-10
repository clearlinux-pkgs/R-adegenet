#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-adegenet
Version  : 2.1.5
Release  : 36
URL      : https://cran.r-project.org/src/contrib/adegenet_2.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/adegenet_2.1.5.tar.gz
Summary  : Exploratory Analysis of Genetic and Genomic Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-adegenet-lib = %{version}-%{release}
Requires: R-ade4
Requires: R-ape
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-igraph
Requires: R-reshape2
Requires: R-seqinr
Requires: R-shiny
Requires: R-vegan
BuildRequires : R-ade4
BuildRequires : R-ape
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-igraph
BuildRequires : R-reshape2
BuildRequires : R-seqinr
BuildRequires : R-shiny
BuildRequires : R-vegan
BuildRequires : buildreq-R

%description
data. Adegenet provides formal (S4) classes for storing and handling
    various genetic data, including genetic markers with varying ploidy
    and hierarchical population structure ('genind' class), alleles counts
    by populations ('genpop'), and genome-wide SNP data ('genlight'). It
    also implements original multivariate methods (DAPC, sPCA), graphics,
    statistical tests, simulation tools, distance and similarity measures,
    and several spatial methods. A range of both empirical and simulated
    datasets is also provided to illustrate various methods.

%package lib
Summary: lib components for the R-adegenet package.
Group: Libraries

%description lib
lib components for the R-adegenet package.


%prep
%setup -q -c -n adegenet
cd %{_builddir}/adegenet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633890525

%install
export SOURCE_DATE_EPOCH=1633890525
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc adegenet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/adegenet/CITATION
/usr/lib64/R/library/adegenet/DESCRIPTION
/usr/lib64/R/library/adegenet/INDEX
/usr/lib64/R/library/adegenet/Meta/Rd.rds
/usr/lib64/R/library/adegenet/Meta/data.rds
/usr/lib64/R/library/adegenet/Meta/features.rds
/usr/lib64/R/library/adegenet/Meta/hsearch.rds
/usr/lib64/R/library/adegenet/Meta/links.rds
/usr/lib64/R/library/adegenet/Meta/nsInfo.rds
/usr/lib64/R/library/adegenet/Meta/package.rds
/usr/lib64/R/library/adegenet/NAMESPACE
/usr/lib64/R/library/adegenet/R/adegenet
/usr/lib64/R/library/adegenet/R/adegenet.rdb
/usr/lib64/R/library/adegenet/R/adegenet.rdx
/usr/lib64/R/library/adegenet/dapcServer/server.R
/usr/lib64/R/library/adegenet/dapcServer/ui.R
/usr/lib64/R/library/adegenet/data/H3N2.rda
/usr/lib64/R/library/adegenet/data/dapcIllus.rda
/usr/lib64/R/library/adegenet/data/datalist
/usr/lib64/R/library/adegenet/data/eHGDP.rda
/usr/lib64/R/library/adegenet/data/hybridtoy.RData
/usr/lib64/R/library/adegenet/data/microbov.rda
/usr/lib64/R/library/adegenet/data/nancycats.rda
/usr/lib64/R/library/adegenet/data/rupica.RData
/usr/lib64/R/library/adegenet/data/sim2pop.rda
/usr/lib64/R/library/adegenet/data/spcaIllus.rda
/usr/lib64/R/library/adegenet/data/swallowtails.rda
/usr/lib64/R/library/adegenet/files/AFLP.txt
/usr/lib64/R/library/adegenet/files/exampleSnpDat.snp
/usr/lib64/R/library/adegenet/files/mondata1.rda
/usr/lib64/R/library/adegenet/files/mondata2.rda
/usr/lib64/R/library/adegenet/files/nancycats.dat
/usr/lib64/R/library/adegenet/files/nancycats.gen
/usr/lib64/R/library/adegenet/files/nancycats.gtx
/usr/lib64/R/library/adegenet/files/nancycats.str
/usr/lib64/R/library/adegenet/files/pdH1N1-HA.fasta
/usr/lib64/R/library/adegenet/files/pdH1N1-NA.fasta
/usr/lib64/R/library/adegenet/files/pdH1N1-data.csv
/usr/lib64/R/library/adegenet/files/swallowtails_loc.csv
/usr/lib64/R/library/adegenet/files/usflu.fasta
/usr/lib64/R/library/adegenet/help/AnIndex
/usr/lib64/R/library/adegenet/help/adegenet.rdb
/usr/lib64/R/library/adegenet/help/adegenet.rdx
/usr/lib64/R/library/adegenet/help/aliases.rds
/usr/lib64/R/library/adegenet/help/paths.rds
/usr/lib64/R/library/adegenet/html/00Index.html
/usr/lib64/R/library/adegenet/html/R.css
/usr/lib64/R/library/adegenet/tests/testthat.R
/usr/lib64/R/library/adegenet/tests/testthat/Rplots.pdf
/usr/lib64/R/library/adegenet/tests/testthat/test-findclust.R
/usr/lib64/R/library/adegenet/tests/testthat/test-genind2genpop.R
/usr/lib64/R/library/adegenet/tests/testthat/test-prop.R
/usr/lib64/R/library/adegenet/tests/testthat/test-seppop.R
/usr/lib64/R/library/adegenet/tests/testthat/test_accessors.R
/usr/lib64/R/library/adegenet/tests/testthat/test_compoplot.R
/usr/lib64/R/library/adegenet/tests/testthat/test_constructors.R
/usr/lib64/R/library/adegenet/tests/testthat/test_conversion.R
/usr/lib64/R/library/adegenet/tests/testthat/test_genlight.R
/usr/lib64/R/library/adegenet/tests/testthat/test_haploGen.R
/usr/lib64/R/library/adegenet/tests/testthat/test_hierarchy.R
/usr/lib64/R/library/adegenet/tests/testthat/test_import.R
/usr/lib64/R/library/adegenet/tests/testthat/test_repool.R
/usr/lib64/R/library/adegenet/tests/testthat/test_snapclust.R
/usr/lib64/R/library/adegenet/tests/testthat/test_subset.R
/usr/lib64/R/library/adegenet/tests/testthat/test_summary.R
/usr/lib64/R/library/adegenet/tests/testthat/test_xval.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/adegenet/libs/adegenet.so
/usr/lib64/R/library/adegenet/libs/adegenet.so.avx2
/usr/lib64/R/library/adegenet/libs/adegenet.so.avx512
