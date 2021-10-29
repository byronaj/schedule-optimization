<!-- Landing page after log in -->

<template>
  <div class="columns">
    <div class="column is-one-fifth">
      <MiniCal />
    </div>
    <div class="column">
      <button class="button buttons-calendar">
        <span class="icon is-small">
          <img src="@/assets/export.svg" @click="exportCalendar" />
        </span>
      </button>
        <ExportCalendar v-if="showExport" ref="EXC" />
      <Calendar v-if="!showExport" ref="FullCalendar"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Calendar from '@/components/layout/Calendar.vue'
import MiniCal from '@/components/layout/MiniCal.vue'
import ExportCalendar from '@/components/layout/ExportCalendar.vue'

export default {
  components: {Calendar, MiniCal, ExportCalendar},
  name: 'Dashboard',
  methods: {
    exportCalendar() {
      this.showExport = !this.showExport
      //window.print()
    }
  },
  data() {
    return {
      showExport: false,
    }
  }
}
</script>

<style scoped>
.buttons-calendar {
  cursor: pointer;
  position: absolute;
  right: 33px;
}
</style>