<template>
    <nav>
        <v-app-bar app color="#2596be">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-btn icon :to="routeHome" class="mr-2">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <v-app-bar-title class="text-uppercase">
                <span class="font-weight-light white--text">Library</span>
                <span class="white--text">Zapps | Staff</span>
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <span class="font-weight-light white--text ">Welcome,</span>
            <span class="white--text mr-6">staff</span>
            <v-btn @click="logout()" color="grey">
                <span>Sign Out</span>
                <v-icon right>mdi-arrow-right</v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer app v-model="drawer" color="#2596be" width="22%">
            <v-list>
                <v-list-group
                    v-for="item in items"
                    :key="item.title"
                    v-model="item.active"
                    >
                    <template v-slot:activator>
                    <v-list-item-action>
                        <v-icon class="white--text">{{item.action}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="white--text" v-text="item.title"></v-list-item-title>
                    </v-list-item-content>
                    </template>

                    <v-list-item
                    v-for="child in item.items"
                    :key="child.title"
                    :to="child.route"
                    >
                        <v-list-item-action>
                            <v-icon class="white--text ml-6">{{child.icon}}</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title class="white--text" v-text="child.title"></v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
import Login from "../services/Login.js"
import axios from "axios";
export default {
    data(){
        return {
            loginService: new Login(),
            route: "/login",
            routeHome: "/",
            drawer: false,
            items: [

                {
                   action: 'mdi-svg',
                    active: false,
                    items: [
                        {title : 'Daftar Buku',icon : 'mdi-playlist-check',route : '/listBukuStaff'},
                      
                    ],  
                    title: 'Buku',  
                },
            
                 {
                   action: 'mdi-book',
                    active: false,
                    items: [
                       {title : 'Daftar Buku Pinjam',icon : 'mdi-playlist-check',route : '/peminjamanStaff'},
                      
                    ],
                    title: 'Peminjaman Buku',  
                },


                {
                    action: 'mdi-account-star',
                    active: false,
                    items: [
                        {title : 'Daftar Pengembalian',icon : 'mdi-playlist-check',route : '/returnBooksView'},
                        

                    ],
                    title: 'Pengembalian Buku',
                },

                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                        { title: 'Profile staff', icon: 'mdi-sort-variant', route: '/profileStaff'},
                      
                    ],
                    title: 'User staff',
                },
             
             
            ],

        }
    },

    methods: {
        logout() {
            this.route = "/login"
            location.replace("/login")
            axios.post('/api/logout')
            this.loginService.removeUserType()
           
        }
    },
}
</script>

<style>
    .v-navigation-drawer__content::-webkit-scrollbar-track{
        -webkit-box-shadow: inset 0 0 6px #5d5d5d;
        background-color: #5d5d5d;
    }
    .v-navigation-drawer__content::-webkit-scrollbar{
        width: 0px;
    }
    .v-navigation-drawer__content::-webkit-scrollbar-thumb{
        -webkit-box-shadow: inset 0 0 6px #424242;
        background-color: #424242;
    }
    #border{
        border-radius: 50%;
    }
</style>