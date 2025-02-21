function init() {
  echo "Initializing AI Code Directory";
  cd ..;
  mkdir ai-gen
  cd ai;
}

function clean() {
  echo "Cleaning up AI Code Directory";
  cd ..;
  rm -rf ai-gen;
  cd ai;
}
