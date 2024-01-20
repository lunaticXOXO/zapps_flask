<template>
  <v-app class="grey lighten-4">
    <div v-if="idRole == 'Guest'">
      <SidebarGuest />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-if="idRole == 1">
      <SidebarAdmin />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 2">
      <SidebarStaff />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    <div v-else-if="idRole == 3">
      <SidebarMember />
      <v-main>
        <router-view/>
      </v-main>
    </div>
    
  </v-app>
</template>

<script>
import SidebarGuest from './components/SidebarGuest.vue'
import SidebarAdmin from './components/SidebarAdmin.vue'
import SidebarStaff from './components/SidebarStaff.vue'
import SidebarMember from './components/SidebarMember.vue'
import Login from "./services/Login.js"

export default {
  name: 'App',
  components: {
    SidebarGuest,
    SidebarAdmin,
    SidebarStaff,
    SidebarMember,
   
},

  mounted() {
    this.fetchData();
  },

  data: () => {
    const data = [];
      return {
          idRole: null,
          username : '',
          iduser : null,
          loginService: new Login(),
          data,
      };
  },

  methods: {
    async fetchData() {
        this.idRole = this.loginService.getCurrentUserType();
        this.username = this.loginService.getCurrentUsername();
        this.iduser = this.loginService.getID();
        console.log(this.idRole)
        console.log(this.username)
        console.log(this.iduser)
    },
  },
};
</script>
