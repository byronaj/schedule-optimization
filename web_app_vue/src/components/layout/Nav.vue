<template>
    <nav class="navbar is-dark has-shadow" role="navigation" aria-label="main navigation" style="min-height: 4rem;">
        <div class="navbar-brand">
            <a class="navbar-item is-size-4" href="/">Schedule Optimizer</a>
            <span class="navbar-burger">
                <span></span>
                <span></span>
                <span></span>
            </span>
        </div>
        <div id="navbar" class="navbar-menu">
            <div class="navbar-start">
                <a href="/" class="navbar-item">Home</a>
                <a href="/about" class="navbar-item">About</a>
            </div>
            <div class="navbar-end">
                <div class="navbar-item is-active">
                    <div class="buttons">
                        <a href="/sign-up" class="button is-primary is-outlined">Sign Up</a>
                        <a href="/log-in" class="button is-success is-outlined"><strong>Log in</strong></a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Nav'
}
</script>