"""Custom topology example

Two directly connected switches plus a host for each switch:

   host1 --- switch --- switch --- host
               | 
   host2 ----- |

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1', ip='10.0.0.1/8' )
        leftHost2 = self.addHost( 'h2', ip='10.0.0.2/8' )
        rightHost = self.addHost( 'h3', ip='10.0.0.3/8' )
        leftSwitch = self.addSwitch( 's4' )
        rightSwitch = self.addSwitch( 's5' )

        # Add links
        self.addLink( leftHost1, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }
