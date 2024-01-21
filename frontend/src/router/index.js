import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
//Member
import ListBooksView from '../views/member/ListBooksView.vue'
import ListBooksBorrowMember from '../views/member/ListBooksBorrowMember.vue'
import ListBooksReturnMember from '../views/member/ListBooksReturnMember.vue'

//Staff
import ListBookStaff from '../views/staff/ListBookStaff.vue'
import ListDetailBooksStaff from '../views/staff/ListDetailBooksStaff.vue'
import ProfileStaff from '../views/staff/ProfileStaff.vue'
import PeminjamanView from '../views/staff/PeminjamanView.vue'
import DetailPeminjamanView from '../views/staff/DetailPeminjamanView.vue'
import ReturnBooksView from '../views/staff/ReturnBooksView.vue'
import PengembalianByIdBorrow from '../views/staff/PengembalianByIdBorrow.vue'
import PelanggaranByPeminjam from '../views/staff/PelanggaranByPeminjam.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomeView,
    meta: {
      title: "Home"
    }
  },


  {
    path: '/login',
    name: 'LoginPage',
    component: LoginView,
    meta: {
      title: "Login"
    }
  },

  //Member
 {
    path : '/listbuku',
    name : 'BooksPage',
    component : ListBooksView,
    meta : {
      title : "Daftar Buku"
    }

 },

 {
    path : '/listBookMember',
    name : 'ListBookMember',
    component : ListBooksBorrowMember,
    meta : {
      title : "Daftar Buku Pinjam"
    }

 },

 {
    path : '/listReturnMember',
    name : 'ListReturnMember',
    component : ListBooksReturnMember,
    meta : {
      title : "Daftar Buku Kembali"
    }

 },

 //Staff

 {
    path : '/listBukuStaff',
    name : 'ListBookStaff',
    component : ListBookStaff,
    meta : {
      title : "Daftar Buku Staff"
    }
 },

 {
    path : '/listBukuDetailStaff/:id',
    name : 'ListBooksDetailStaff',
    component : ListDetailBooksStaff,
    meta : {
      title : "Daftar detail buku"
    }

 },

 {
    path : '/profileStaff',
    name : 'ProfileStaff',
    component : ProfileStaff,
    meta : {
      title : "Profile Staff"
    }
 },

 {
    path : '/peminjamanStaff',
    name : 'PeminjamanStaff',
    component : PeminjamanView,
    meta : {
      title : "Peminjaman Staff"
    }
 },

 {

    path : '/detailPeminjamanStaff/:id',
    name : 'DetailPeminjamanStaff',
    component : DetailPeminjamanView,
    meta : {
      title : "Detail Peminjaman Staff"
    }
 },

 {

  path : '/returnBooksView',
  name : 'ReturnBooksStaff',
  component : ReturnBooksView,
  meta : {
    title : "Pengembalian Buku"
  }


 },

 {
    path : '/pengembalian/:id',
    name : 'ReturnBookByIdPinjam',
    component : PengembalianByIdBorrow,
    meta : {
      title : "Pengembalian Buku by ID Pinjam"
    }

 },

 {
  path : '/violationPeminjam/:id',
  name : 'PelanggaranByPeminjam',
  component : PelanggaranByPeminjam,
  meta : {
    title : "Denda untuk peminjam"
  }
 }



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
  // `/nested`'s will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if(nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else if(previousNearestWithMeta) {
    document.title = previousNearestWithMeta.meta.title;
  }

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if(!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    // We use this to track which meta tags we create so we don't interfere with other ones.
    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  })
  // Add the meta tags to the document head.
  .forEach(tag => document.head.appendChild(tag));

  next();
});

export default router
