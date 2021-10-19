<template>
  <div class="modal is-active" tabindex="-1" role="dialog">
    <div class="modal-background" v-on:click="close"></div>
    <div class="modal-card">
      <slot></slot>
    </div>
    <button class="modal-close is-large" aria-label="close" v-on:click="close"></button>
  </div>
</template>

<script>
export default {
  name: "Modal",
  methods: {
    close() {
      document.removeEventListener('keydown', this.handleKeydown);
      this.$emit('close');
    },
    handleKeydown(e) {
      if (e.target === this.$el && e.keyCode === 27) {
        e.preventDefault();
        this.close();
      }
    }
  },
  mounted() {
    this.$el.focus();
    document.addEventListener('keydown', this.handleKeydown);
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.handleKeydown);
  }
}
</script>

<style scoped>

</style>