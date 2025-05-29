Vagrant.configure("2") do |config|
  config.vm.define "dynatrace" do |dynatrace|
    dynatrace.vm.box = "debian/bookworm64"
    dynatrace.vm.hostname = "dynatrace"

    dynatrace.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 2
    end
  end
end

