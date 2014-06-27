The Choose Your Own Adventure README for Nova
=============================================

You have come across a cloud computing fabric controller.  It has identified
itself as "Nova."  It is apparent that it maintains compatibility with
the popular Amazon EC2 and S3 APIs.

To monitor it from a distance: follow `@openstack <http://twitter.com/openstack>`_ on twitter.

To tame it for use in your own cloud: read http://docs.openstack.org

To study its anatomy: read http://nova.openstack.org

To dissect it in detail: visit http://github.com/openstack/nova

To taunt it with its weaknesses: use http://bugs.launchpad.net/nova

To watch it: http://jenkins.openstack.org

To hack at it: read HACKING

To cry over its pylint problems: http://jenkins.openstack.org/job/nova-pylint/violations

SolidFire Replication Additions
=============================================

What's included in this branch:
1. Ability to set extra-specs (requires modified novaclient as well: https://github.com/j-griffith/python-novaclient/tree/essex-volume-types-extra-specs)
2. Modified SolidFire driver (san.py) to check for volume-types that include replication info

How it works:
Admin creates a volume-type with extra-specs that denote the remote-replication cluster
    `nova volume-type-create rep replication:mvip=192.168.139.136 replication:login=remote-mvip-login replication:pasword=remot-mvip-password`

User now creates a volume as usual, however can specify a replicated type if they wish:
    `nova volume-create --volume_type rep --display_name my-replicated-volume 100`

What the code does for you:
1. Driver gets the create call as usual

2. Now checks to see if there's a volume-type associated with the Volume

3. Extracts remote cluster info from replication type extra-specs if present

4. If not a replicated type, just ignore and do as we've alway done

5. If the volume is of type "replication":

   - Setup cluster pairing between *this* SF Cluster and the specified Remote

   - Create a Volume on both *this* SF Cluster and the specified Remote

   - Enable Volume-Pairing on the two volumes

6. On delete, if the volume is paired, delete on both the source and target SF Clusters
