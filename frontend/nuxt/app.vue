<template>
  <main class="main">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </main>
</template>

<style scoped>
.main {
  padding: 40px;
  margin: 10px;

  border: 2px solid var(--color-accent);
  border-radius: 12px;
  background: var(--color-background);

  height: 100%;
  /* width: 100%; */
  overflow: hidden;
}
</style>