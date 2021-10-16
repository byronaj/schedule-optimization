<!-- Landing page after log in -->

<template>
    <div class="left">
        <div class="minical">Mini Calendar</div>
    </div>
    <div class="right">
        <Calendar />
    </div>
</template>

<script>
import Calendar from '../components/layout/Calendar.vue'

// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  components: { Calendar },
    name: 'Dashboard'
}
</script>

<style scoped>
    .left {
        display: inline-block;
        width: 300px;
    }
    .right {
        display: inline-block;
        width: 100%;
    }
    .minical {
        width: 300px;
        height: 300px;
        display: inline-block;
    }
    .top {
        height: 150px;
        display: inline-block;
    }
</style>