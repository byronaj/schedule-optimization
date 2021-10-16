<template>
<!--    <section class="hero is-info is-large">-->
    <div v-if="!loggedIn" class="home">
        <section class="section hero is-medium is-primary is-bold">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <p class="title">
                        Welcome to Schedule Optimizer
                    </p>
                    <p class="subtitle">
                        An automatic shift scheduler
                    </p>
                </div>
            </div>
        </section>
    </div>
    <div v-else class="home loggedin" style="display: inline-flex;">
        <Dashboard />
    </div>
<!--    </section>-->
</template>

<script>

// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Dashboard from '@/views/Dashboard'

export default {
    name: 'Home',
    components: {
        Dashboard
    },
    data() {
        return {
            loggedIn: true,
            isAdmin: true
        }
    }
}
</script>

<style>
    .home {
        width: 100%;
    }
</style>