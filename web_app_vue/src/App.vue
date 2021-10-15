<template>
    <div>
        <Header />

        <router-view />

        <Footer />
    </div>
</template>

<script>
import Header from '@/components/layout/Header'
import Nav from '@/components/layout/Nav'
import Footer from '@/components/layout/Footer'

export default {
    name: 'App',
    components:{
        Header,
        Nav,
        Footer
    }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
