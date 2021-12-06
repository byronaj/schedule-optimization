<template >

    <template v-if="$store.state.user.isAuthenticated">
        <section class="section hero is-fullheight" style="padding: 0; min-height: 1px">
            <div class="hero-body" style="padding: 10px 0">
                <div class="container is-fluid">
                    <Dashboard />
                </div>
            </div>
        </section>
    </template>

    <template v-else>
        <section class="section hero is-fullheight-with-navbar is-primary is-bold">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <p class="title">Welcome to Schedule Optimizer</p>
                    <p class="subtitle">An automatic shift scheduler</p>
                </div>
            </div>
        </section>
    </template>

</template>

<script>
import HomeAuthenticated from '@/views/HomeAuthenticated';
import HomeUnauthenticated from '@/views/HomeUnauthenticated';
import Dashboard from '@/views/Dashboard';

export default {
    name: 'Home',
    components: {
        HomeAuthenticated,
        HomeUnauthenticated,
        Dashboard,
    },
    data() {
        return {
            componentKey: 0,
        };
    },
};
</script>

<style></style>
