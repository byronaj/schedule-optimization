<!-- Landing page after log in -->

<template>
  <div class="columns">
    <div class="column is-one-fifth">
      Mini Calendar
    </div>
    <div class="column">
      <Calendar/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Calendar from '@/components/layout/Calendar.vue'

export default {
  components: {Calendar},
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