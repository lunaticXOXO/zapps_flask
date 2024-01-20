<template>
    <nav>
        <v-app-bar app color="#2596be">
            <v-app-bar-title class="text-uppercase">
                <span class="font-weight-light white--text">Library</span>
                <span class="white--text">Zapps</span>
            </v-app-bar-title>
          
            <v-spacer></v-spacer>
            <v-btn :to="route" color="grey">
                <span>Login</span>
                <v-icon right>mdi-key</v-icon>
            </v-btn>
        </v-app-bar>
    </nav>
</template>

<script>
export default {
    data(){
        return {
            route: "/login",
            routeHome: "/",
        }
    }
}
</script>

<style>
    #border{
        border-radius: 50%;
    }
</style>