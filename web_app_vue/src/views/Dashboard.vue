<!-- Landing page after log in -->

<template>
  <div class="columns">
    <div class="column is-one-fifth">
      <MiniCal ref="MiniCal"/>
      <DisplayConstraints />
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
import DisplayConstraints from '@/components/layout/DisplayConstraints.vue'

export default {
  components: {Calendar, MiniCal, ExportCalendar, DisplayConstraints},
  name: 'Dashboard',
  methods: {
    exportCalendar() {
      let ev = null
      let current = null
      if (!this.showExport) { //pull events before FullCalendar is hidden
        ev = this.$refs.FullCalendar.getEvents()
        current = this.$refs.FullCalendar.getDate();
      }

      this.showExport = !this.showExport

      if (this.showExport) {
        setTimeout(() => { //because the FullCalendar doesn't open up fast enough
          try {
            this.$refs.EXC.setDate(current);
            this.$refs.EXC.setEvents(ev); //send events to Export View
          }
          catch { }
        }, 100);
      }
      
      setTimeout(() => { //because the FullCalendar doesn't open up fast enough
        try {
          let resDate = this.$refs.MiniCal.getDate();
          this.$refs.FullCalendar.changeDate(resDate); //can be executed only when FullCalendar is showing, so this will execute only when hiding the Export view
        }
        catch { }
      }, 100);
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