<!-- Landing page after log in -->

<template>
  <div class="columns">
    <div class="column is-one-fifth">
      <MiniCal/>
    </div>
    <div class="column">
      <div class="is-one-fifth buttons-calendar"><img src="@/assets/export.svg" @click="exportCalendar" />
        <!--<ExportCalendar v-if="showExport" />-->
      </div>
      <Calendar ref="FullCalendar"/>
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

.buttons-calendar {
  width: 50px;
  height: 50px;
  cursor: pointer;
  position: absolute;
  right: 20px;
  border-radius: 26px;
  border: #000 solid 1px;
  text-align: center;
  padding: 5px 0px 0px 5px;
}
.buttons-calendar img {
  height: 35px;
  width: 35px;
}
</style>