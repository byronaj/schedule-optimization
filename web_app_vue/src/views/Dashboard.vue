<!-- Landing page after log in -->

<template>
  <div class="columns">
    <div class="column is-one-fifth">
      <MiniCal/>
    </div>
    <div class="column">
      <Calendar ref="FullCalendar"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Calendar from '@/components/layout/Calendar.vue'
import MiniCal from '@/components/layout/MiniCal.vue'

export default {
  components: {Calendar, MiniCal},
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