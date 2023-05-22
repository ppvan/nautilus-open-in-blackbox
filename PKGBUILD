# Maintainer: Pham Phuc <phuclaplace@gmail.com>

pkgname=nautilus-open-in-blackbox
pkgver=1.0.0
pkgrel=1
pkgdesc="Open current directory in BlackBox from Nautilus context menu"
arch=('any')
url="https://github.com/ppvan/OpenInBlackBox"
license=('GPL3')
depends=('python-nautilus>=4.0')
makedepends=('git')

_commit=6a6254b1b70a60efb65812fee60e3eedbff4c7f3
source=("git+https://github.com/ppvan/OpenInBlackBox#commit=$_commit")

sha256sums=('SKIP')

_dest='/usr/share/nautilus-python/extensions'

package() {
    cd "$srcdir/$pkgname"
    mkdir -p "$_dest"
    cp blackbox_extension.py "$_dest"

    nautilus -q
}