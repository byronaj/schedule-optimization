<!-- Landing page after log in -->

<template>
    <div class="home">
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
