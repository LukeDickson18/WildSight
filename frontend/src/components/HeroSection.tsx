function Hero() {
  return (
    <section className="mx-auto flex max-w-6xl flex-col items-center px-8 py-24 text-center">
      <h1 className="mb-6 text-5xl font-bold text-slate-900">
        Discover, Record, and Analyze Wildlife
      </h1>

      <p className="mb-10 max-w-3xl text-lg text-slate-600">
        Build your personal wildlife journal, identify species,
        explore your observations, and uncover patterns in nature.
      </p>

      <div className="flex gap-4">
        <button className="rounded-lg bg-green-700 px-6 py-3 font-semibold text-white transition hover:bg-green-800">
          Log a Sighting
        </button>

        <button className="rounded-lg border border-green-700 px-6 py-3 font-semibold text-green-700 transition hover:bg-green-50">
          Explore Species
        </button>
      </div>
    </section>
  );
}

export default Hero;