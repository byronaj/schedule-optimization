<template>
  <div id="myCal"></div>
</template>

<script>
import Calendar from "color-calendar";
import "color-calendar/dist/css/theme-glass.css";

export default {
  name: "ColorCalendar",
  mounted() {
    new Calendar({
      id: "#myCal",
      calendarSize: "small",
      /*disableDayClick: "true",*/
      theme: "glass"
    });
  }
};
</script>