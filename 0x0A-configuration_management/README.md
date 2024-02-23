# Configuration Management README

## Introduction to Configuration Management

Configuration Management is a crucial aspect of modern IT infrastructure management. It refers to the process of systematically handling changes to a system in a way that maintains its integrity over time. This involves tracking and controlling changes to configurations, ensuring consistency, and automating repetitive tasks to streamline operations.

### Benefits of Configuration Management:
- **Consistency**: Ensures that all systems are configured identically, reducing errors caused by configuration discrepancies.
- **Efficiency**: Automates repetitive tasks, saving time and effort for administrators.
- **Scalability**: Allows for easy management of large-scale environments with numerous servers and devices.
- **Compliance**: Facilitates adherence to security and regulatory requirements by enforcing standardized configurations.
- **Recovery**: Simplifies disaster recovery by enabling quick restoration of configurations to known states.

## Puppet Resource Type: File

Puppet is a powerful configuration management tool that uses a declarative language to describe system configurations. One of the fundamental resource types in Puppet is the `file` resource, which is used to manage files and directories on a system.

### Example Manifest:
```puppet
file { '/etc/example.conf':
  ensure  => present,
  content => "This is an example configuration file.\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
```

In this example:
- `ensure`: Ensures that the file exists (`present`) or does not exist (`absent`).
- `content`: Specifies the content of the file.
- `owner`: Sets the owner of the file.
- `group`: Sets the group of the file.
- `mode`: Sets the permissions of the file.

## Puppet's Declarative Language: Modeling Instead of Scripting

Puppet uses a declarative language that allows administrators to describe the desired state of a system, rather than writing procedural scripts to achieve that state. This approach abstracts away the implementation details, focusing instead on the end result.

### Declarative vs. Imperative:
- **Declarative**: Describes what should be done without specifying how it should be done.
- **Imperative**: Specifies the exact steps to achieve a desired outcome.

By using a declarative language, Puppet simplifies configuration management and makes it easier to maintain configurations over time.

## Puppet Lint

Puppet Lint is a tool used to analyze Puppet code for style and syntax errors. It helps ensure that Puppet manifests adhere to best practices and maintain consistency across configurations.

### Example Usage:
```bash
puppet-lint my_manifest.pp
```

Puppet Lint can catch various issues such as missing documentation, improper indentation, and deprecated language constructs, helping to improve the overall quality of Puppet codebases.

## Puppet Emacs Mode

Puppet Emacs Mode is an Emacs major mode designed to provide syntax highlighting and indentation support for Puppet manifests within the Emacs text editor.

### Features:
- Syntax highlighting for Puppet language constructs.
- Automatic indentation to maintain code readability.
- Integration with other Emacs features such as code navigation and auto-completion.

Puppet Emacs Mode enhances the development experience for Puppet administrators who prefer using Emacs as their text editor.

---

# The trifecta

Package/file/service: Learn it, live it, love it. Even if this is the only Puppet you know, you can still get a whole lot done.
```puppet
package { 'openssh-server':
  ensure => installed,
}

file { '/etc/ssh/sshd_config':
  source  => 'puppet:///modules/sshd/sshd_config',
  owner   => 'root',
  group   => 'root',
  mode    => '0640',
  notify  => Service['sshd'], # sshd restarts whenever you edit this file.
  require => Package['openssh-server'],
}

service { 'sshd':
  ensure => running,
  enable => true,
}
```

## file

Manages files, directories, and symlinks.

### Important attributes
- ensure – Whether the file should exist, and what it should be. Allowed values:
  - file (a normal file)
  - directory (a directory)
  - link (a symlink)
  - present (anything)
  - absent
- path – The full path to the file on disk; defaults to title.
- owner – By name or UID.
- group – By name or GID.
- mode – Must be specified exactly. Does the right thing for directories.

### For normal files

- source – Where to download contents for the file. Usually a puppet:/// URL.
- content – The file’s desired contents, as a string. Most useful when paired with templates, but you can also use the output of the file function.

### For directories

- source – Where to download contents for the directory, when recurse => true.
- recurse – Whether to recursively manage files in the directory.
- purge – Whether unmanaged files in the directory should be deleted, when recurse => true.

### For symlinks

- target – The symlink target. (Required when ensure => link.)

### Other notable attributes

- backup
- checksum
- force
- ignore
- links
- recurselimit
- replace

## package
Manages software packages.

### Important attributes
- name – The name of the package, as known to your packaging system; defaults to title.
- ensure – Whether the package should be installed, and what version to use. Allowed values:
  - present
  - latest (implies present)
  - any version string (implies present)
  - absent
  - purged (Potentially dangerous. Ensures absent, then zaps configuration files and dependencies, including those that other packages depend on. Provider-dependent.)
- source – Where to obtain the package, if your system’s packaging tools don’t use a repository.
- provider – Which packaging system to use (e.g. Yum vs. Rubygems), if a system has more than one available.

## service
Manages services running on the node. Like with packages, some platforms have better tools than others, so read up.

You can make services restart whenever a file changes, with the `subscribe` or `notify` metaparameters. For more info, read the related topic about relationships

### Important attributes
- name – The name of the service to run; defaults to title.
- ensure – The desired status of the service. Allowed values:
  - running (or true)
  - stopped (or false)
- enable – Whether the service should start on boot. Doesn’t work on all systems.
- hasrestart – Whether to use the init script’s restart command instead of stop+start. Defaults to false.
- hasstatus – Whether to use the init script’s status command. Defaults to true.

### Other notable attributes
If a service has a bad init script, you can work around it and manage almost anything using the `status, start, stop, restart, pattern, and binary` attributes.

---
## Conclusion

Configuration Management, facilitated by tools like Puppet, plays a critical role in maintaining the stability, consistency, and scalability of IT infrastructures. By leveraging Puppet's declarative language, administrators can efficiently manage system configurations, enforce best practices, and automate repetitive tasks, ultimately contributing to smoother operations and improved system reliability. Additionally, tools like Puppet Lint and Puppet Emacs Mode further enhance the development and maintenance of Puppet manifests, ensuring code quality and consistency across environments.
